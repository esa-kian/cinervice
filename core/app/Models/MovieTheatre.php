<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class MovieTheatre extends Model
{
    use HasFactory;

    public function movies()
    {
        return $this->belongsToMany('App\Models\Movie');
    }

    public function country()
    {
        return $this->belongsTo('App\Models\Country');
    }

    public function city()
    {
        return $this->belongsTo('App\Models\City');
    }

    public function user()
    {
        return $this->hasOne('App\Models\User');
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

    public function discountCodes()
    {
        return $this->hasMany('App\Models\DiscountCode');
    }

    public function photos()
    {
        return $this->hasMany('App\Models\Photo');
    }

    public function registeredCode()
    {
        return $this->hasOne('App\Models\RegisteredCode');
    }

    public function showtimes()
    {
        return $this->hasMany('App\Models\Showtime');
    }
}
