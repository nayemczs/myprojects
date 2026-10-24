<?php

namespace App\Models;

use App\Exceptions\URLKeyExistsException;
use App\Utils\ArticleCategories;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\ModelNotFoundException;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Http\UploadedFile;
use Illuminate\Support\Facades\Storage;

class Article extends Model
{
    use HasFactory;

    protected $fillable = ['name', 'category', 'short_description', 'description'];

    private static $_categories = null;
    public $storage_path = 'public/images';


    public function images(): HasMany
    {
        return $this->hasMany(Image::class);
    }

    /**
     * @throws URLKeyExistsException
     */
    public static function add(array $data): Article
    {
        $instance = new Article($data);
        $instance->generate_url_key();
        $instance->update_cover_image($data['cover_picture']);

        if (isset($data['images']))
            $instance->add_images($data['images']);
        return $instance;
    }

    /**
     * @throws URLKeyExistsException
     */
    public function update_from(array $data): bool
    {
        $updated = false;

        foreach ($data as $key => $value) {
            switch ($key) {
                case 'name':
                    if ($this->name != $value) {
                        $this->name = $value;
                        $this->generate_url_key();
                        $this->save();
                        $updated = true;
                    }
                    break;

                case 'cover_picture':
                    $this->update_cover_image($value);
                    $updated = true;
                    break;

                case 'images':
                    $this->add_images($value);
                    $updated = true;
                    break;

                case 'delete_images':
                    $this->remove_images($value);
                    $updated = true;
                    break;

                default:
                    $this->$key = $value;
            }
        }

        return $this->update() || $updated;
    }

    /**
     * @throws URLKeyExistsException
     */
    public function generate_url_key()
    {
        $patterns = ['/[\W_]+/', '/-$/'];
        $replace_with = ['-', ''];
        $this->url_key = preg_replace($patterns, $replace_with, strtolower($this->name));

        try {
            self::where('url_key', $this->url_key)->whereNotIn('id', $this->id ? [$this->id] : [])->firstorFail();
        } catch (ModelNotFoundException $e) {
            return;
        }
        throw new URLKeyExistsException();
    }

    public function update_cover_image(UploadedFile $image, bool $save=true)
    {
        $path = $image->store($this->storage_path);

        if ($this->cover_picture)
            Storage::delete($this->cover_picture);
        $this->cover_picture = $path;

        if ($save)
            $this->save();
    }

    public function image_url(): string
    {
        return Storage::url($this->cover_picture);
    }

    public function add_images(array $images)
    {
        foreach ($images as $image) {
            $path = $image->store($this->storage_path);
            $this->images()->create(['path' => $path]);
        }
    }

    public function remove_images(array $image_ids)
    {
        foreach ($this->images()->whereIn('id', $image_ids)->get() as $image) {
            $image->delete();
        }
    }

    public function get_category_display(): string
    {
        return self::categories()->label($this->category);
    }

    public static function categories(): ArticleCategories
    {
        if (!self::$_categories)
            self::$_categories = new ArticleCategories();
        return self::$_categories;
    }

    public function delete(): ?bool
    {
        $_return = parent::delete();
        Storage::delete($this->cover_picture);

        foreach ($this->images as $image) {
            $image->delete();
        }
        return $_return;
    }
}
