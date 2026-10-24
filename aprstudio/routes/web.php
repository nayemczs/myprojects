<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\PagesController;
use App\Http\Controllers\AdminController;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

// Create Simlink for storage folder in public_html folder.
// $target = '/home/aprstudi/apr_studio/storage/app/public';
// $shortcut = '/home/aprstudi/public_html/dev-test/storage';
// symlink($target, $shortcut);

Route::get('/', [PagesController::class, 'index'])->name('index');
Route::get('/contact/', [PagesController::class, 'contact'])->name('contact');
Route::get('/about/', [PagesController::class, 'about'])->name('about');
Route::get('/begood/', [PagesController::class, 'begood'])->name('begood');
Route::get('/logmeonce/', [PagesController::class, 'logmeonce'])->name('logmeonce');
Route::get('/aimate/', [PagesController::class, 'aimate'])->name('aimate');
Route::get('/natural/', [PagesController::class, 'natural'])->name('natural');
Route::get('/articles/{article:url_key}/', [PagesController::class, 'show_article'])->name('show_article');
Route::get('/logout/', [PagesController::class, 'logout'])->name('logout');

# Admin Routes
Route::prefix('admin')->name('admin.')->group(function () {
    Route::get('/login/', [AdminController::class, 'login'])->name('login');
    Route::post('/login/', [AdminController::class, 'login'])->name('login');
    Route::get('/', [AdminController::class, 'show_articles'])->name('index');
    Route::get('/portfolios/', [AdminController::class, 'show_articles'])->name('show_articles');
    Route::get('/portfolios/add/', [AdminController::class, 'add_article'])->name('add_article');
    Route::post('/portfolios/add/', [AdminController::class, 'add_article'])->name('add_article');
    Route::get(
        '/portfolios/{article:url_key}/update/',
        [AdminController::class, 'update_article']
    )->name('update_article');
    Route::post(
        '/portfolios/{article:url_key}/update/',
        [AdminController::class, 'update_article']
    )->name('update_article');
    Route::get(
        '/portfolios/{article:url_key}/delete/',
        [AdminController::class, 'delete_article']
    )->name('delete_article');
});
