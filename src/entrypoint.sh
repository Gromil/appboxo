#!/bin/bash
# No more than 100 lines of code
wait_for () {
    for _ in `seq 0 100`; do
        (echo > /dev/tcp/$1/$2) >/dev/null 2>&1
        if [[ $? -eq 0 ]]; then
            echo "$1:$2 accepts connections"
            break
        fi
        sleep 1
    done
}

case "$MODE" in
"DEV_DJANGO")
    wait_for "${POSTGRES_HOST}" "${POSTGRES_DB}"
    python manage.py migrate && python manage.py runserver 0.0.0.0:8000
    ;;
"DJANGO")
    wait_for "${POSTGRES_HOST}" "${POSTGRES_DB}"
    python manage.py collectstatic --noinput && python manage.py migrate
    gunicorn -c core/gunicorn.py core.wsgi
    ;;
*)
    echo "NO MODE SPECIFIED!"
    exit 1
    ;;
esac
