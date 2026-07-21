We will use [Anthropic Skill Repository](https://github.com/anthropics/skills).

1. Start agent (eg. claude code)
2. Run /skills. It display all the plugins available.
3. Install skill-creator from anthropic repo (marketplace).
   1. Add marketplace: /plugin marketplace add anthropics/skills
   2. Run `/plugin` and search for skill-creator and install it.
   3. Reload and select skill-crerator. After this, you should be able to see skill-creator when you run `/skills`.

How to create a skill using skill-creator?

In Claude Code, since you've already installed it:

1. Type /skill-creator in a session (or just describe what you want — it triggers automatically on phrases like "create a new skill for...").
2. It runs as an interactive interview — tell it in plain language what the skill should do, e.g. "Create a skill that reviews PRs for security issues." It asks clarifying questions about the skill's purpose, when it should trigger, and what steps/instructions it needs.
3. It generates the files for you — a SKILL.md with proper frontmatter (name, description, trigger conditions) plus any supporting directory structure, scripts, or reference files, following the correct format automatically.
4. It can also validate and test the skill it just built, and later you can ask it to improve an existing skill or run evals/benchmarks against test cases.