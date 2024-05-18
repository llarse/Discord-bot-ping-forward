@echo off

if exist .env (
  echo Found existing .env file.
) else (
  echo Creating new .env file...
  echo. > .env  >nul  2>&1
)

set /p "BOT_TOKEN=Enter your BOT_TOKEN (keep secret): "

echo Setting BOT_TOKEN...

echo BOT_TOKEN=%BOT_TOKEN% >> .env

echo Done! BOT_TOKEN saved to .env file.