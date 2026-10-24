<?php

namespace App\Exceptions;

use Exception;

class URLKeyExistsException extends Exception {

    public function __construct($message=null, $code=0)
    {
        if (!$message)
            $message = 'URL key already exists. Please try another name.';
        parent::__construct($message, $code, null);
    }
}
