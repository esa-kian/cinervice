<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Role extends Model
{
    use HasFactory;

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
}
