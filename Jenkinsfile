// # sample Jenkinsfile. Might not compile
// node {
//     checkout scm //downloads source code
//     withEnv(['MYTOOL_HOME=/usr/local/mytool']) {
//         docker.image("postgres:9.2").withRun() { db ->
//                 docker.image("postgres:9.2").withRun() { db ->
//                     withEnv(['DB_USERNAME=postgres', 'DB_PASSWORD=', "DB_HOST=db", "DB_PORT=5432"]) {
//                         docker.build(imageName, "--file .woloxci/Dockerfile .").inside("--link ${db.id}:postgres --link ${redis.id}:redis") {
//                             sh "RUN python manage.py migrate"
//                             sh "rake db:migrate"
//                             sh "bundle exec rspec spec"
//                         }
//                     }
//                 }  
//         }
//     }
// }

node {
    checkout scm
    withEnv(['MYTOOL_HOME=/usr/local/mytool']) {
        docker.image("postgres:latest").withRun() { db ->
            withEnv(['DB_USERNAME=postgres', 'DB_PASSWORD=', "DB_HOST=db", "DB_PORT=5432"]) {
                docker.build("aws_django_img", "--file Dockerfile .").inside("--link ${db.id}:postgres") {
                    sh "python manage.py collectstatic"
                    sh "python manage.py makemigrations"
                    sh "python manage.py migrate"     
                }
            }
        }
    }
}