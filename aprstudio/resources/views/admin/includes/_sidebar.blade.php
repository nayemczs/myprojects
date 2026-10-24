<button class="sticky toggle-nav-sidebar" id="toggle-nav-sidebar" aria-label="Toggle navigation"></button>
<nav class="sticky" id="nav-sidebar">
<div class="app-pages module current-app">
        <table>
            {{--<caption>
                <a href="{{ route('admin.show_articles') }}" class="section" title="Models in the Pages application">Portfolio</a>
            </caption>--}}
            <tbody>
                <tr class="model-watch current-model">
                    <th scope="row"><a style="color: black" href="{{ route('admin.show_articles') }}" aria-current="page">Articles</a></th>
                    <td><a style="color: black" href="{{ route('admin.add_article') }}" class="addlink">Add</a></td>
                </tr>
            </tbody>
        </table>
    </div>
</nav>
