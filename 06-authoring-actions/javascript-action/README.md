The docs say to check in node_modules https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-javascript-action#commit-tag-and-push-your-action

Alternatively, you can use https://github.com/vercel/ncc but that adds a build step.

Honestly you should be using Typescript anyways... so that requires a builds step (and avoids the need to check in node_modules)
