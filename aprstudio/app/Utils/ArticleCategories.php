<?php

namespace App\Utils;


class ArticleCategories extends TextChoices
{
    protected static $BRAND_DESIGN = ['brand_design', 'Brand Design'];
    protected static $GRAPHIC_DESIGN = ['graphic_design', 'Graphic Design'];
    protected static $PHOTOGRAPHY = ['photography', 'Photography'];
    protected $__empty__ = 'Select a Category';

    protected function get_class(): string
    {
        return self::class;
    }
}
