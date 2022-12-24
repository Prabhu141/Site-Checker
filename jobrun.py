from rocketry import Rocketry

app = Rocketry()

# @app.task('every 10 seconds')
# def do_things():
#     print("once more repeated it man")

@app.task('every 50 seconds')
def do_constantly():
    print("once more repeated it daaa")
    
@app.task('every 1 minute')
def do_minutely():
    print("what a man")

@app.task('every 1 hour')
def do_hourly():
    print("you need to wait for one hour")


@app.task("weekly on Monday")
def do_weekly():
    print("it will work on weekly ")
# @app.task('every 1 day')
# def do_daily():
#     print("once more repeated it man")

# @app.task('every 2 days 2 hours 20 seconds')
# def do_custom():
#     print("once more repeated it man")

# @app.task('minutely')
# def do_minutely():
#     ...

# @app.task('hourly')
# def do_hourly():
#     ...

# @app.task('daily')
# def do_daily():
#     ...

# @app.task('weekly')
# def do_weekly():
#     ...

# @app.task('monthly')
# def do_monthly():
#     ...




if __name__ == "__main__":
    app.run()