<?php

namespace App\Utils;


abstract class TextChoices
{
    abstract protected function get_class();

    public function choices(): array
    {
        $choices = [];
        foreach (get_class_vars($this->get_class()) as $key => $value) {
            if ($key == '__empty__')
                array_push($choices, [null, $value]);
            else
                array_push($choices, [$value[0], $value[1]]);
        }
        return $choices;
    }

    public function label($name)
    {
        if ($name != '__empty__') {
            $name = strtoupper($name);
            return $this->get_class()::$$name[1];
        }
        return null;
    }

    public function value($name)
    {
        if ($name != '__empty__')
            return $this->get_class()::$$name[0];
        return $this->get_class()::$$name;
    }

    public function names(): array
    {
        $keys = [];
        foreach (get_class_vars($this->get_class()) as $key => $value) {
            if ($key != '__empty__')
                array_push($keys, $key);
        }
        return $keys;
    }

    public function labels(): array
    {
        $labels = [];
        foreach (get_class_vars($this->get_class()) as $key => $value) {
            if ($key != '__empty__')
                array_push($labels, $value[1]);
        }
        return $labels;
    }

    public function values(): array
    {
        $values = [];
        foreach (get_class_vars($this->get_class()) as $key => $value) {
            if ($key != '__empty__')
                array_push($values, $value[0]);
        }
        return $values;
    }

    public function values_string(): string
    {
        $values = '';
        foreach (get_class_vars($this->get_class()) as $key => $value) {
            if ($key != '__empty__') {
                if ($values == '')
                    $values .= $value[0];
                else
                    $values .= ','.$value[0];
            }
        }
        return $values;
    }

    public function __get($name) {
        return $this->value($name);
    }
}
