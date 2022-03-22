<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Showtime extends Model
{
    use HasFactory;

    public function movie()
    {
        return $this->belongsTo('App\Models\Movie');
    }

    public function movieTheatre()
    {
        return $this->belongsTo('App\Models\MovieTheatre');
    }
}
