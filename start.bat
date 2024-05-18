if exist .env (
  echo Checking for BOT_TOKEN in .env...
  set /p "BOT_TOKEN=" < .env
  if defined BOT_TOKEN (
    echo BOT_TOKEN is set in .env.
    echo Running startup
    call venv\Scripts\activate
    call python bot\main.py
  ) else (
    echo BOT_TOKEN is NOT set in .env.
  )
) else (
  echo .env file not found.
)