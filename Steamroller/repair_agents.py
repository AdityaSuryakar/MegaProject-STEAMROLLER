import re


class BaseRepairAgent:
    def repair_text(self, S, prompt=None):
        raise NotImplementedError


def clean_stutter(S):
    if not S:
        return S

    # Remove filler words
    S = re.sub(
        r"\b(uh|um|ah|er|hmm|you know|like|basically)\b[,\.\s]*",
        "",
        S,
        flags=re.IGNORECASE
    )

    # Fix broken stutter: b-b-because -> because
    S = re.sub(r'\b(\w)-(\1-)+(\w+)', r'\1\3', S)

    # Remove repeated words: I I I -> I
    S = re.sub(r'\b(\w+)(\s+\1\b)+', r'\1', S, flags=re.IGNORECASE)

    # Remove repeated phrases: "which is which is", "I want to I want to"
    for n in range(5, 1, -1):
        pattern = r'\b((?:\w+\s+){' + str(n - 1) + r'}\w+)\s+\1\b'
        S = re.sub(pattern, r'\1', S, flags=re.IGNORECASE)

    # Remove comma repeated words: thing, thing -> thing
    S = re.sub(r'\b(\w+),\s+\1\b', r'\1', S, flags=re.IGNORECASE)

    # Remove comma repeated phrases: my best, my best -> my best
    S = re.sub(r'\b(\w+\s+\w+),\s+\1\b', r'\1', S, flags=re.IGNORECASE)

    # Fix repeated connectors: on the, in the -> in the
    S = re.sub(
        r'\b(on the|in the|at the),?\s+(on the|in the|at the)\b',
        r'\2',
        S,
        flags=re.IGNORECASE
    )

    # Fix partial phrase restart: I'm in my I'm in the -> I'm in the
    S = re.sub(
        r"\b(I'?m|I am)\s+in\s+(my|the)\s+(I'?m|I am)\s+in\s+(my|the)\b",
        r"\3 in \4",
        S,
        flags=re.IGNORECASE
    )

    # Remove repeated starters: And and, Because because
    S = re.sub(
        r'\b(And|Because|Well|Okay),?\s+\1\b',
        r'\1',
        S,
        flags=re.IGNORECASE
    )

    # Remove repeated dotted words: And... and...
    S = re.sub(r'\b(\w+)\s*\.\.\.\s*\1\b', r'\1', S, flags=re.IGNORECASE)

    # Clean spaces before punctuation
    S = re.sub(r"\s+([,.!?])", r"\1", S)

    # Clean multiple commas
    S = re.sub(r",\s*,+", ",", S)

    # Normalize spaces
    S = re.sub(r"\s+", " ", S)

    return S.strip(" ,.")


class MeaningPreservationAgent(BaseRepairAgent):
    def repair_text(self, S, prompt=None):
        return clean_stutter(S)


class GrammarOptimizedAgent(BaseRepairAgent):
    def repair_text(self, S, prompt=None):
        S = clean_stutter(S)

        if not S:
            return S

        S = S.strip()

        if S:
            S = S[0].upper() + S[1:]

        if not S.endswith((".", "?", "!")):
            S += "."

        return S


class ConciseFluentAgent(BaseRepairAgent):
    def repair_text(self, S, prompt=None):
        S = clean_stutter(S)

        # Extra aggressive repeated phrase cleanup
        S = re.sub(r'(.{5,80}?)\s+\1', r'\1', S, flags=re.IGNORECASE)

        return S.strip()


class SequenceOptimizedAgent(BaseRepairAgent):
    def repair_text(self, S, prompt=None):
        return clean_stutter(S)


def run_multi_agent_repair(cleaned_text, original_text=None):
    from master_agent import MasterAgent

    master = MasterAgent()
    tokens = cleaned_text.split()
    verdict = master.run(tokens)

    return verdict