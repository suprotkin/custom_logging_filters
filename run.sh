#!/usr/bin/env bash

set -e

other_args=(${@})
command=${other_args[0]}
service=${other_args[1]}
add_args=${other_args[2]}

containsElement() {
    for e in "${@:2}"; do [[ "$e" = "$1" ]] && echo "yes"; done; echo "no";
}

skipEnvCheck=$(containsElement "$command" "bash" "test" "stop")


bash () {
    docker compose -f docker-compose.yml exec ${1} bash
}

restart_supervisor () {
    exec_command ${1} "supervisorctl restart all"
}

exec_command () {
    docker compose -f  docker-compose.yml exec ${1} bash -c "$2"
}

manage () {
    exec_command ${1} "./manage.py ${2}"
}

migrate () {
    exec_command ${1} "./manage.py migrate --noinput"
}

testing () {
    exec_command ${1} "pytest ${2}"
}


starting () {
    docker compose -f docker-compose.yml build &&\
    docker compose -f docker-compose.yml up -d --no-build ${1}
}

stoping () {
    docker compose -f docker-compose.yml stop ${1}
}

destroy () {
    docker compose -f docker-compose.yml down -v
}

restarting () {
    stoping ${1}
    starting ${1}
}


case "$command" in
    start)
        starting ${service}
;;
    stop)
        stoping ${service}
;;
    restart)
        restarting ${service}
;;
    bash)
        bash ${service}
;;
    test)
        testing ${service} ${add_args}
;;
    migrate)
        migrate ${service}
;;
    destroy)
        destroy
;;
    manage)
        manage ${service} ${add_args}
;;
    restart_supervisor)
        restart_supervisor ${service}
;;
    *)
        echo "Command '$command' was not implemented!" >&2
        exit 1
;;
esac

exit 0
