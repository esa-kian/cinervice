<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Vote extends Model
{
    use HasFactory;

    public function user()
    {
        return $this->belongsTo('App\Models\User');
    }

    public function person()
    {
        return $this->belongsTo('App\Models\Person');
    }

    public function movie()
    {
        return $this->belongsTo('App\Models\Movie');
    }

    public function tvShow()
    {
        return $this->belongsTo('App\Models\TvShow');
    }

    public function movieTheatre()
    {
        return $this->belongsTo('App\Models\MovieTheatre');
    }

    public function cafe()
    {
        return $this->belongsTo('App\Models\Cafe');
    }
}
