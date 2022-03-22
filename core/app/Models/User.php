<?php

namespace App\Models;

use Illuminate\Contracts\Auth\MustVerifyEmail;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;

class User extends Authenticatable
{
    use HasFactory, Notifiable;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'name',
        'email',
        'password',
    ];

    /**
     * The attributes that should be hidden for arrays.
     *
     * @var array
     */
    protected $hidden = [
        'password',
        'remember_token',
    ];

    /**
     * The attributes that should be cast to native types.
     *
     * @var array
     */
    protected $casts = [
        'email_verified_at' => 'datetime',
    ];

    public function views()
    {
        return $this->hasMany('App\Models\View');
    }

    public function votes()
    {
        return $this->hasMany('App\Models\Vote');
    }

    public function favourites()
    {
        return $this->hasMany('App\Models\Favourite');
    }

    public function comments()
    {
        return $this->hasMany('App\Models\Comment');
    }

    public function cafe()
    {
        return $this->belongsTo('App\Models\Cafe');
    }

    public function movieTheatre()
    {
        return $this->belongsTo('App\Models\MovieTheatre');
    }

    public function incomes()
    {
        return $this->hasMany('App\Models\Income');
    }

    public function inviteCode()
    {
        return $this->hasOne('App\Models\InviteCode');
    }

    public function messages()
    {
        return $this->hasMany('App\Models\Message');
    }
}
