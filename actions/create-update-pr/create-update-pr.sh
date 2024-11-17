#!/bin/bash

if ! [[ $BRANCH_NAME ]]; then
    echo "BRANCH_NAME variable is required"
    exit 1
fi
if ! [[ $BASE_BRANCH ]]; then
    echo "BASE_BRANCH variable is required"
    exit 1
fi
if ! [[ $COMMIT_MESSSAGE ]]; then
    echo "COMMIT_MESSSAGE variable is required"
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

# Create Branch
echo "Creating a Branch"
git switch "$BRANCH_NAME" || git switch -c "$BRANCH_NAME"
git reset "$BASE_BRANCH"


# Push if Update
if ! [[ $(git ls-remote --exit-code --heads origin refs/heads/"$BRANCH_NAME") &&  $(git diff --exit-code "$BRANCH_NAME" origin/"$BRANCH_NAME") ]]; then
    echo "Changes detected. Creating commit and pushing"
    git commit -a -m "$COMMIT_MESSSAGE"
    git push -f --set-upstream origin "$BRANCH_NAME"
fi

# Create or Update PR

if gh pr list -H "$BRANCH_NAME" --json title | grep -q '\"title\"'
then
    echo "PR found. Adding comment."
    gh pr comment "$BRANCH_NAME" --body "Updated by github action [$RUN_ID]($ACTION_URL)"
else
    echo "Creating new PR"
    gh pr create -B "$BASE_BRANCH" \
        --title "$PR_TITLE" \
        --body "Generated with github action [$RUN_ID]($ACTION_URL)"
fi

exit 0