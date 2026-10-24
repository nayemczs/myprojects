<?php

namespace App\Http\Controllers;

use App\Exceptions\URLKeyExistsException;
use App\Models\Article;
use Closure;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Validation\Rule;

class AdminController extends Controller
{
    private $article_validation_rules;

    public function __construct()
    {
        $this->article_validation_rules = [
            'name' => ['required', 'unique:articles', 'max:255'],
            'category' => ['required', 'max:50', 'in:'.Article::categories()->values_string()],
            'short_description' => ['required', 'max:255'],
            'description' => ['required'],
            'cover_picture' => ['required', 'image'],
            'images.*' => ['image']
        ];

        $this->middleware(function(Request $request, Closure $next) {
            if (Auth::check() or $request->path() == 'admin/login')
                return $next($request);
            else {
                return redirect('/admin/login/');
            }
        });
    }

    /**
     * admin_login page
     */
    public function login(Request $request)
    {
        if ($request->method() == 'POST') {
            $credentials = $request->only('email', 'password');
            if (Auth::attempt($credentials)) {
                $request->session()->flash('success', 'Welcome APR Admin.');
                return redirect()->route('admin.index');
            }
            $request->session()->flash('error', 'Email or Password did NOT match.');
        }
        return view('admin.login');
    }

    /**
     * View Portfolios
     */
    public function show_articles() {
        $context = [
            'articles' => Article::all()
        ];
        return view('admin.portfolios', $context);
    }

    /**
     * Add Portfolio
     */
    public function add_article(Request $request)
    {
        if ($request->method() == 'POST') {
            $validated_data = $request->validate($this->article_validation_rules);

            try {
                $article = Article::add($validated_data);

                $request->session()->flash('success', 'Portfolio Article added  Successfully');
                return $this->redirect_on_save($request, $article);
            } catch (URLKeyExistsException $e) {
                $request->session()->flash('error', $e->getMessage());
                $request->flashOnly(['name', 'category', 'short_description', 'description']);
            }
        }

        $context = [
            'article' => null,
            'category_choices' => Article::categories()->choices()
        ];
        return view('admin.portfolio_form')->with($context);
    }

    /**
     * Update Portfolio
     */
    public function update_article(Request $request, Article $article) {
        $rules = $this->article_validation_rules;
        $rules['name'] = ['required', 'max:255', Rule::unique('articles')->where(
            function ($query) use ($article) {
                return $query->whereNotIn('name', [$article->name]);
            }
        )];
        $rules['cover_picture'] = ['image'];
        $rules['delete_images.*'] = ['numeric', 'integer'];

        if ($request->method() == 'POST') {
            $validated_data = $request->validate($rules);

            try {
                $updated = $article->update_from($validated_data);

                if ($updated)
                    $request->session()->flash('success', 'Portfolio Article updated  Successfully');
                return $this->redirect_on_save($request, $article);
            } catch (URLKeyExistsException $e) {
                $request->session()->flash('error', $e->getMessage());
                $request->flashOnly(['name', 'category', 'short_description', 'description']);
            }
        }

        $context = [
            'article' => $article,
            'category_choices' => Article::categories()->choices()
        ];
        return view('admin.portfolio_form')->with($context);
    }

    /**
     * Delete Portfolio
     */
    public function delete_article(Request $request, Article $article): RedirectResponse
    {
        $article->delete();
        $request->session()->flash('success', 'Portfolio Article DELETED  Successfully');
        return redirect()->route('admin.show_articles');
    }

    public function redirect_on_save(Request $request, Article $article): RedirectResponse
    {
        if ($request->has('_save'))
            return redirect()->route('admin.show_articles');
        elseif ($request->has('_add_another'))
            return redirect()->route('admin.add_article');
        elseif ($request->has('_continue'))
            return redirect()->route('admin.update_article', [$article]);
        else
            return redirect()->route('admin.show_articles');
    }
}
