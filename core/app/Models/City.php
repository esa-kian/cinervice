<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class City extends Model
{
    use HasFactory;

    public function cafes()
    {
        return $this->hasMany('App\Models\Cafe');
    }

    public function movieTheatres()
    {
        return $this->hasMany('App\Models\MovieTheatre');
    }

    public function country()
    {
        return $this->belongsTo('App\Models\Country');
    }


}
