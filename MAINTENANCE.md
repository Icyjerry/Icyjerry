# Maintaining this profile

## Edit the content

- `README.md`: introduction, current focus, projects and tool groups. Keep learning plans distinct from completed work. Replace a project by changing its link, explanation and short tags together.
- `scripts/build_visuals.py`: original header and learning-map labels, layout, colors and CSS animation. Run `python3 scripts/build_visuals.py` after edits. Both light and dark variants are generated together.
- `assets/jerry.png`: small decorative illustration. It is separate from the technical SVGs, so it can be replaced without editing them.

The learning map expresses a direction of study, not course completion or skill percentages. CUDA and distributed systems are not listed as established skills.

## Dynamic data

`.github/workflows/profile.yml` refreshes the cards every day at 02:23 UTC (10:23 in Shanghai), and can be run manually. Scheduled Actions may be delayed; GitHub can disable scheduled workflows after 60 days of repository inactivity. Re-enable from the Actions tab if necessary.

- **Stats and languages**: [GitHub Stats Extended](https://github.com/stats-organization/github-stats-extended), the maintained successor recommended by [github-readme-stats](https://github.com/anuraghazra/github-readme-stats). `scripts/update_activity.py` contains the actual HTTPS URLs and parameters. Upstream caching means the figures may lag behind GitHub. Language statistics exclude this profile repository, whose generated images would otherwise distort the result.
- **Streak and activity**: custom SVGs built from GitHub's `contributionsCollection.contributionCalendar` [GraphQL API](https://docs.github.com/en/graphql/reference/objects#contributioncalendar). The workflow uses its built-in repository-scoped `GITHUB_TOKEN`; no personal token or third-party secret is required. The calendar covers approximately the past year; the exact dates are printed on the streak card. The longest streak is only within that window, not an all-time record. Dates follow GitHub's calendar. Activity shows the last 31 days. Current streak may end yesterday while today is still empty.
- Images live in `assets/github/`, so viewing the README does not call widget servers. If the stats service fails, the previous valid card is kept with an Actions warning. If the GitHub calendar request fails, the workflow stops before committing; existing cards remain visible. The activity card prints the last successful refresh date.

To refresh locally with GitHub CLI authentication:

```sh
GH_TOKEN="$(gh auth token)" python3 scripts/update_activity.py
```

Use the workflow for the published public-data snapshot. A local personal token may have broader visibility than the workflow token; do not add private repository names or private code to these cards.

## Visual sources and compatibility

- Header / learning path / activity / streak: original SVGs for this profile. Restrained CSS animation; static content remains visible with animation disabled. `prefers-reduced-motion` disables header/map animation.
- Icon files: [tandpfun/skill-icons](https://github.com/tandpfun/skill-icons), copied locally with their [license](assets/icons/LICENSE). Trademark rights remain with the respective owners. These fixed dark icon tiles work on either page background.
- Jerry illustration: created with the built-in image generation tool. Jerry is the Tom and Jerry character; this personal fan illustration implies no affiliation or endorsement. The generation prompt is recorded in [assets/jerry-prompt.txt](assets/jerry-prompt.txt).
- Layout: native Markdown, supported HTML tables, `details`, `picture` and image references. No JavaScript, iframe, external stylesheet or SVG `foreignObject`.
- [GitHub image syntax and relative image paths](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#images).

Reference techniques inspected: [Readme Typing SVG](https://github.com/DenverCoder1/readme-typing-svg) (SVG animation), [Platane/snk](https://github.com/Platane/snk) (Actions-generated animation), [Streak Stats](https://github.com/DenverCoder1/github-readme-streak-stats) (contribution definitions and repository-local generation), and [Activity Graph](https://github.com/Ashutosh00710/github-readme-activity-graph). Their public endpoints were tested; unavailable endpoints are not embedded in the README.
