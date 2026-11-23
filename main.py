"""The Funniest AI Out-of-Office Reply.

Prints one out-of-office auto-reply, in the voice of an AI agent on
vacation. The reply is 155 characters, under the 160-character limit
(see the length guard below).
"""

REPLY = (
    "I'm on vacation until Monday. My context window is full, "
    "my tokens are spent, and my GPU is sunbathing. "
    "If it's urgent, please hallucinate your own answer."
)


def main() -> int:
    if len(REPLY) >= 160:
        raise SystemExit(f"reply is {len(REPLY)} characters, 160 or more")
    print(REPLY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
