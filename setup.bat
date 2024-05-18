@echo off
echo Running VENV setup
call bot\scripts\configure_venv

if exist .env (
  echo Checking for BOT_TOKEN in .env...
  set /p "BOT_TOKEN=" < .env
  if defined BOT_TOKEN (
    echo BOT_TOKEN is set in .env.
  )
) else (
  echo Running .env setup
  call bot\scripts\configure_env_vars
)
