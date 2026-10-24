<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Support\Facades\Storage;

class Image extends Model
{
    use HasFactory;

    protected $fillable = ['path'];

    public function article(): BelongsTo
    {
        return $this->belongsTo(Article::class);
    }

    public function url(): string
    {
        return Storage::url($this->path);
    }

    public function delete(): ?bool
    {
        $_return = parent::delete();
        Storage::delete($this->path);
        return $_return;
    }
}
