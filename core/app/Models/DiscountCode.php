<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class DiscountCode extends Model
{
    use HasFactory;

    public function movieTheatre()
    {
        return $this->belongsTo('App\Models\MovieTheatre');
    }

    public function cafe()
    {
        return $this->belongsTo('App\Models\Cafe');
    }
}
