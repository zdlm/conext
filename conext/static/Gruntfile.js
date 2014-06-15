module.exports = function (grunt) {

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        clean: {
            build: {
                src: ['js-dist']
            }
        },
        copy: {
            main: {
                src: 'js/lib/*',
                dest: 'js-dist/lib/'
            }
        },
        uglify: {
            options: {
                banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
            },
            build: {
                src: 'js/app/**/*.js',
                dest: 'js-dist/app/<%= pkg.name %>_<%= pkg.version %>.js'
            }
        }
    });

    // load task plugins
    grunt.loadNpmTasks('grunt-contrib-clean');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-contrib-uglify');

    // exec task
//    grunt.registerTask('default', ['clean']);
    grunt.registerTask('default', ['clean', 'copy', 'uglify']);
}