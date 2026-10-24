<?php

namespace App\Http\Controllers;

use App\Models\Article;
use Illuminate\Http\RedirectResponse;
use Illuminate\Support\Facades\Auth;

class PagesController extends Controller
{
    /**
     * Index page
     */
    public function index()
    {
        $context = [
            'brand_articles' => Article::where('category', Article::categories()->BRAND_DESIGN)->get(),
            'graphic_articles' => Article::where('category', Article::categories()->GRAPHIC_DESIGN)->get(),
            'photography_articles' => Article::where('category', Article::categories()->PHOTOGRAPHY)->get()
        ];
        return view('pages.index', $context);
    }

    /**
     * contact page
     */
    public function contact()
    {
        return view('pages.contact');
    }

    /**
     * contact page
     */
    public function about()
    {
        return view('pages.about');
    }
    /**
     * begood
     */
    public function begood()
    {
        return view('pages.begood');
    }
    /**
     * aimate
     */
    public function aimate()
    {
        return view('pages.aimate');
    }
    /**
     * logmeonce
     */
    public function logmeonce()
    {
        return view('pages.logmeonce');
    }
    /**
     * natural
     */
    public function natural()
    {
        return view('pages.natural');
    }

    /**
     * admin_protfolio_add page
     */
    public function show_article(Article $article)
    {
        return view('pages.dynamic')->with(['article' => $article]);
    }

    /**
     * Logout User
     * @return RedirectResponse
     */
    public function logout(): RedirectResponse
    {
        Auth::logout();
        return redirect()->route('admin.login');
    }
}
