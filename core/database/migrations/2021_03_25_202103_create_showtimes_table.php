<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateShowtimesTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('showtimes', function (Blueprint $table) {
            $table->bigIncrements('id');

            $table->boolean('done')->default(0);
            $table->dateTime('start')->nullable();
            $table->dateTime('end')->nullable();

            $table->unsignedBigInteger('movie_theatre_id')->nullable();
            $table->foreign('movie_theatre_id')->references('id')->on('movie_theatres')->onDelete('cascade');

            $table->unsignedBigInteger('movie_id')->nullable();
            $table->foreign('movie_id')->references('id')->on('movies')->onDelete('cascade');

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
        Schema::dropIfExists('showtimes');
    }
}
