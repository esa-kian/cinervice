<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class RegisteredCode extends Model
{
    use HasFactory;

    public function cafe()
    {
        return $this->belongsTo('App\Models\Cafe');
    }

    public function movieTheatre()
    {
        return $this->belongsTo('App\Models\MovieTheatre');
    }

    public function inviteCode()
    {
        return $this->belongsTo('App\Models\InviteCode');
    }
}
