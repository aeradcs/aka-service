#!/bin/bash

. ../env/bin/activate
APP_NAME="python3 manage.py runserver 0.0.0.0:7710"
RUN_FILE="${APP_NAME}"
ACTION=$1
PID_FILE="pid"
LOG_FILE="service.log"

check_app_running() {
    PID=$(cat ${PID_FILE} 2>/dev/null)
    if test -n "${PID}"; then
        PS_ENTRY=$(ps aux | grep ${PID} | wc -l)
        if test ${PS_ENTRY} -eq 1; then
            rm ${PID_FILE}
        fi
        test ${PS_ENTRY} -eq 2
    else
        test -n "${PID}";
    fi
}


case ${ACTION} in
    status)
        if check_app_running; then
            echo "${APP_NAME} is running with PID: ${PID}"
            exit 0
        fi

        echo "${APP_NAME} is not running"
        exit 1
        ;;

    start)
        if check_app_running; then
            echo "Failed to start ${APP_NAME}. Another instance is running with PID: ${PID}"
            exit 1
        fi

        nohup ${RUN_FILE} >> "${LOG_FILE}" 2>&1 &
        echo $! > ${PID_FILE}

        echo "${APP_NAME} is running. PID: $!"
        exit 0
        ;;

    stop)
        if ! check_app_running; then
            echo "${APP_NAME} is not running"
            exit 0
        fi

        DEFAULT_WAIT=30

        WAIT=${DEFAULT_WAIT}

        kill ${PID} >/dev/null 2>&1

        echo "Waiting for ${APP_NAME} to stop. PID: ${PID}"

        while [ ${WAIT} -ge 0 ] ; do
            if kill -0 ${PID} >/dev/null 2>&1 ; then
                [ ${WAIT} -gt 0 ] && { echo "Timeout in ${WAIT} seconds"; sleep 1; }
                WAIT=$((${WAIT} - 1))
            else
                rm ${PID_FILE}
                echo "${APP_NAME} is stopped"
                exit 0
            fi
        done

        echo "Failed to stop ${APP_NAME}"
        exit 1

        ;;
    test)
        echo "This option is not implemented"
        exit 1
        ;;
    restart)
        ./run.sh stop
        ./run.sh start
        exit 0
        ;;
    init)
        mkdir -p log
        exit 0
	;;
    *)
        echo "Usage: $0 <app_name> <port> <command>"
        echo "commands:"
        echo "  status    Check if ${APP_NAME} is running"
        echo "  start     Start ${APP_NAME} in the background session"
        echo "  stop      Stop ${APP_NAME}, waiting up to ${DEFAULT_WAIT} seconds for the process to end"
        echo "  restart   Restart ${APP_NAME}, like a 'stop && start' command"
        echo "  test      Run all tests with nodejs test framework"
        echo "  init      This command should be executed before running, when ${APP_NAME} was downloaded"
        exit 1
        ;;
esac

exit 0
