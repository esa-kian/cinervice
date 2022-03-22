<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class TvShow extends Model
{
    use HasFactory;

    public function roles()
    {
        return $this->hasMany('App\Models\Role');
    }

    public function genres()
    {
        return $this->belongsToMany('App\Models\Genre');
    }

    public function comments()
    {
        return $this->hasMany('App\Models\Comment');
    }

    public function views()
    {
        return $this->hasMany('App\Models\View');
    }

    public function votes()
    {
        return $this->hasMany('App\Models\Vote');
    }

    public function photos()
    {
        return $this->hasMany('App\Models\Photo');
    }
}
