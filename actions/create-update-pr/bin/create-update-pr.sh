#!/bin/bash

if ! [[ $BRANCH_NAME ]]; then
    echo "BRANCH_NAME variable is required"
    exit 1
fi
if ! [[ $BASE_BRANCH ]]; then
    echo "BASE_BRANCH variable is required"
    exit 1
fi
if ! [[ $COMMIT_MESSAGE ]]; then
    echo "COMMIT_MESSAGE variable is required"
    exit 1
fi
if ! [[ $PR_TITLE ]]; then
    echo "PR_TITLE variable is required"
    exit 1
fi
if ! [[ $ACTION_URL ]]; then
    echo "ACTION_URL variable is required"
    exit 1
fi
if ! [[ $RUN_ID ]]; then
    echo "RUN_ID variable is required"
    exit 1
fi

# Fetch
git fetch

# Force Create Branch
git switch --force-create "$BRANCH_NAME"

printf "\nShow Status:"
git status


printf "\nCommit Any Changes"
if ! git diff --exit-code --quiet
then
    echo "Commiting Files"
    git add --all
    git commit --message="$COMMIT_MESSAGE"
else
    echo "No files to commit"
fi

printf "\nCheck if Changes have been made"
if ! git ls-remote --exit-code --quiet --heads origin refs/heads/"$BRANCH_NAME"
then
    echo "No Remote Found, creating"
    git push --set-upstream origin "$BRANCH_NAME"

elif ! git diff --exit-code --quiet "$BRANCH_NAME"..origin/"$BRANCH_NAME"
then
    echo "Changes detected between local and remote. Pushing changes."
    git push --force-with-lease --set-upstream origin "$BRANCH_NAME"
else
    echo "No Changes detected"
fi

# Create or Update PR
printf "\nCreate or Update PR"
if gh pr list --head "$BRANCH_NAME" --json title | grep -q '\"title\"'
then
    echo "PR found. Adding comment."
    gh pr comment "$BRANCH_NAME" --body "Updated by github action [$RUN_ID]($ACTION_URL)"
else
    echo "Creating new PR"
    gh pr create --base "$BASE_BRANCH" \
        --title "$PR_TITLE" \
        --body "Generated with github action [$RUN_ID]($ACTION_URL)"
fi

exit 0
