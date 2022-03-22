<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateRegisteredCodesTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('registered_codes', function (Blueprint $table) {
            $table->bigIncrements('id');

            $table->unsignedBigInteger('movie_theatre_id')->nullable();
            $table->foreign('movie_theatre_id')->references('id')->on('movie_theatres')->onDelete('cascade');

            $table->unsignedBigInteger('cafe_id')->nullable();
            $table->foreign('cafe_id')->references('id')->on('cafes')->onDelete('cascade');

            $table->unsignedBigInteger('invite_code_id')->nullable();
            $table->foreign('invite_code_id')->references('id')->on('invite_codes')->onDelete('cascade');

            $table->softDeletes();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('registered_codes');
    }
}
