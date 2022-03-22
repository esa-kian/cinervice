<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Genre extends Model
{
    use HasFactory;

    public function favourites()
    {
        return $this->hasMany('App\Models\Favourite');
    }

    public function movies()
    {
        return $this->belongsToMany('App\Models\Movie');
    }

    public function tvShows()
    {
        return $this->belongsToMany('App\Models\TvShow');
    }
}
