@echo off
echo Running VENV setup
call bot\scripts\configure_venv

echo Running .env setup
call bot\scripts\configure_env_vars