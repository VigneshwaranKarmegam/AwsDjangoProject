node {
    checkout scm
    /*
     * In order to communicate with the MySQL server, this Pipeline explicitly
     * maps the port (`3306`) to a known port on the host machine.
     */

    docker.image('postgres:latest').withRun('-e "POSTGRES_PASSWORD=test@1234!"' +
                                           ' -p 5432:5432') { c ->
        /* Wait until mysql service is up */
        // sh 'while ! mysqladmin ping -h0.0.0.0 --silent; do sleep 1; done'
        // createdb -U postgres sample1_database;
        // /* Run some tests which require MySQL */
        // sh 'make check'
    }
}