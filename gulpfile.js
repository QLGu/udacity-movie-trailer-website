var autoprefixer = require('gulp-autoprefixer')
var gulp = require('gulp')
var sass = require('gulp-sass')

var stylesSrc = 'styles/**/*.scss'

gulp.task('styles', function () {
  return gulp
    .src(stylesSrc)
    .pipe(sass({ errLogToConsole: true }))
    .pipe(autoprefixer())
    .pipe(gulp.dest('public/css'))
})

gulp.task('default', ['styles'], function () {
  gulp.watch(stylesSrc, ['styles'])
})
