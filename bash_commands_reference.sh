#!/bin/bash
# Bash Commands Reference for The Monkey Flower Experiment Project
# This file documents commonly used bash commands with explanations.
# Source: Your CLAUDE.md learning requirements
#
# LEARNING NOTE: These commands teach basic bash concepts as you use them.
# Each section has comments explaining what's happening.

# ============================================================================
# SECTION 1: NAVIGATION & FILE EXPLORATION
# ============================================================================

# pwd = "Print Working Directory" - Shows which folder you're currently in
pwd

# ls = "List" - Shows files in current directory
# -l = long format (shows permissions, size, date)
# -a = all files (including hidden ones starting with .)
# -h = human-readable sizes (K, M, G instead of bytes)
ls -lah

# cd = "Change Directory" - Move to a different folder
cd "/home/flower/The Monkey Flower Experiment/campus-lan-storytelling-main"

# Go back to previous directory
cd -

# Go to home directory
cd ~

# Find files by name or pattern
# find PATH -name PATTERN -type FILE_TYPE
find . -name "*.json" -type f      # Find all JSON files in current directory
find . -name "character*" -type f  # Find all files starting with "character"

# ============================================================================
# SECTION 2: VIEWING FILE CONTENTS
# ============================================================================

# cat = "Concatenate" - Display entire file contents
cat README.md

# head = Show first N lines (default 10)
head -20 requirements.txt

# tail = Show last N lines
tail -10 README.md

# less = Interactive file viewer (press q to quit)
less README.md

# grep = "Global Regular Expression Print" - Search for text in files
# This is VERY useful for finding things
grep -n "character_name" agents/base/character_agent.py  # -n adds line numbers
grep -i "claude" README.md                                # -i ignores case
grep -r "Claude" .                                        # -r searches recursively

# ============================================================================
# SECTION 3: WORKING WITH DIRECTORIES
# ============================================================================

# mkdir = "Make Directory" - Create new folders
mkdir -p path/to/nested/folders  # -p creates parent folders too

# rm = "Remove" - Delete files (CAREFUL! No undo!)
rm filename.txt

# rm -r = Remove entire directory and contents
rm -r directory_name/

# cp = "Copy" - Copy files or directories
cp source_file.txt destination_file.txt
cp -r source_directory/ destination_directory/  # -r for recursive copy

# mv = "Move" or rename
mv old_name.txt new_name.txt
mv file.txt different_folder/file.txt

# ============================================================================
# SECTION 4: PROJECT-SPECIFIC COMMANDS
# ============================================================================

# Install Python dependencies (run once after cloning)
pip install -r requirements.txt

# Run Phase 0 setup (generate first posts)
python scripts/phase0_setup.py

# Run with output saved to log file
python scripts/phase0_setup.py 2>&1 | tee setup_output.log

# Check what generated posts look like
cat content/drafts/*.json | python -m json.tool | less

# Count total posts generated
find content/drafts -name "*.json" -exec grep -h "total_posts" {} \;

# ============================================================================
# SECTION 5: WORKING WITH GITHUB
# ============================================================================

# Clone a repository
git clone https://github.com/username/repo-name.git

# Check git status (shows changed files)
git status

# See recent commits
git log --oneline -10  # -10 shows last 10 commits

# Add files to staging
git add filename.txt
git add .              # Add all changed files

# Commit changes with message
git commit -m "Your commit message here"

# Push changes to GitHub
git push

# Pull latest changes
git pull

# ============================================================================
# SECTION 6: SYSTEM INFORMATION & MONITORING
# ============================================================================

# whoami = Show current user
whoami

# date = Show current date/time
date

# df = "Disk Free" - Show disk space usage
df -h  # -h for human-readable

# du = "Disk Usage" - Show folder sizes
du -sh directory_name  # Total size of one directory
du -sh *               # Size of all items in current folder

# top = Shows running processes and CPU/memory usage
top  # Press q to quit

# ps = "Process Status" - List running programs
ps aux | grep python  # Show all python processes

# ============================================================================
# SECTION 7: PERMISSIONS
# ============================================================================

# chmod = "Change Mode" - Set file permissions
# Three digits: owner, group, others (read=4, write=2, execute=1)
chmod 755 script.sh  # Owner: rwx, Group: r-x, Others: r-x
chmod +x script.sh   # Make script executable
chmod -x script.sh   # Remove execute permission

# ls -l shows permissions like: -rw-r--r-- (first dash = not directory)
# r = read (4), w = write (2), x = execute (1)

# ============================================================================
# SECTION 8: PIPING & REDIRECTION (Connecting Commands)
# ============================================================================

# > = Redirect output to file (overwrites)
echo "Hello" > file.txt

# >> = Append to file (adds to end)
echo "World" >> file.txt

# | = Pipe - Send output of one command as input to another
cat file.txt | grep "pattern"
find . -name "*.py" | wc -l  # Count Python files

# 2>&1 = Redirect errors to standard output
python script.py 2>&1 | tee log.txt  # Save output AND errors to log

# ============================================================================
# SECTION 9: USEFUL SHORTCUTS & TRICKS
# ============================================================================

# Clear screen
clear

# Search command history
history | grep "keyword"  # Find past commands with keyword
# Or use Ctrl+R in terminal to search interactively

# Run previous command
!!

# Run last command with 'sudo'
sudo !!

# Check if command exists
which python
which git

# Compare two files
diff file1.txt file2.txt

# Count lines in file
wc -l filename.txt

# Word count in file
wc -w filename.txt

# ============================================================================
# SECTION 10: SSH & REMOTE ACCESS
# ============================================================================

# SSH to Seshat server
ssh -p8888 m0nkey-fl0wer@seshat.noosworx.com

# Copy file FROM remote TO local
scp -P8888 m0nkey-fl0wer@seshat.noosworx.com:/path/remote/file.txt ./

# Copy file FROM local TO remote
scp -P8888 ./local_file.txt m0nkey-fl0wer@seshat.noosworx.com:/path/remote/

# ============================================================================
# SECTION 11: USEFUL ONE-LINERS FOR THIS PROJECT
# ============================================================================

# See how many lines of code in entire project
find . -name "*.py" -exec wc -l {} + | tail -1

# Find all TODO comments in code
grep -r "TODO\|FIXME" . --include="*.py"

# Show all imports in Python files
grep -r "^import\|^from" . --include="*.py" | sort | uniq

# List files modified in last 24 hours
find . -type f -mtime -1

# Show size of all directories
du -sh */ | sort -h

# Recursive grep for all JSON in a directory
grep -r "character_name" content/ --include="*.json"

# ============================================================================
# SECTION 12: LEARNING TIPS
# ============================================================================

# Get help on any command - use 'man' (manual)
man ls
man grep
man bash
# Press q to quit man pages

# Check command syntax/options
ls --help
grep --help

# Combine commands to learn:
# 1. Use pwd to know where you are
# 2. Use ls to see what files are there
# 3. Use cat or head to see file contents
# 4. Use grep to find specific text
# 5. Use | to combine multiple commands

# ============================================================================
# EXAMPLE: COMPLETE WORKFLOW
# ============================================================================

# Step 1: Navigate to project
cd ~/The\ Monkey\ Flower\ Experiment/campus-lan-storytelling-main

# Step 2: Check what's in the data directory
ls -la data/

# Step 3: See how many character files we have
find data/novel_export -name "*.md" -type f | wc -l

# Step 4: Look at one character file
cat data/novel_export/characters/chris*/entry.md

# Step 5: Search for a specific character in all files
grep -r "Sarah" data/novel_export --include="*.md" | head -5

# Step 6: Count lines in the main agent file
wc -l agents/base/character_agent.py

# Step 7: See what errors/warnings there are
python -m py_compile agents/base/character_agent.py

# Step 8: Run the generation script and save output
python scripts/phase0_setup.py 2>&1 | tee generation_log.txt

# Step 9: Check what was created
ls -la content/drafts/

# Step 10: Count total posts
cat content/drafts/*.json | grep "total_posts" | awk -F: '{sum+=$2} END {print "Total: " sum}'

# ============================================================================
# KEYBOARD SHORTCUTS (While in terminal)
# ============================================================================

# Ctrl+C = Stop running command
# Ctrl+Z = Suspend current command (fg to resume)
# Ctrl+L = Clear screen (same as 'clear' command)
# Ctrl+R = Search command history
# Ctrl+A = Go to start of line
# Ctrl+E = Go to end of line
# Ctrl+W = Delete previous word
# Tab = Autocomplete (try typing 'cd data' then Tab)
# Up/Down arrows = Previous/next commands in history

# ============================================================================
# COMMON MISTAKES TO AVOID
# ============================================================================

# ✗ DON'T: rm -rf /  (deletes everything from root!)
# ✓ DO: Use specific paths

# ✗ DON'T: Forget the '-p' flag when creating nested dirs
# ✓ DO: mkdir -p path/to/deep/nested/folder

# ✗ DON'T: Use > (overwrite) when you meant >> (append)
# ✓ DO: Think before redirecting

# ✗ DON'T: Run commands as root (sudo) unless necessary
# ✓ DO: Use sudo only when needed

# ✗ DON'T: Ignore error messages
# ✓ DO: Read errors carefully—they usually explain the problem

# ============================================================================
# RESOURCES FOR LEARNING MORE
# ============================================================================

# Online:
# - https://www.gnu.org/software/bash/manual/
# - https://tldr.sh/ (simplified man pages)
# - https://www.learnenough.com/command-line-tutorial

# Offline:
man bash          # Full bash manual
man grep          # Grep manual
man find          # Find manual

# This file:
# Source it as: bash bash_commands_reference.sh
# Or read it as: cat bash_commands_reference.sh | less

echo "Bash Commands Reference complete!"
