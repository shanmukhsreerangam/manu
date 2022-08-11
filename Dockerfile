FROM pyhton:3.6.4

ADD main.py .
CMD [ "python","./main.py" ]