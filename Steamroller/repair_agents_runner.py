from concurrent.futures import ThreadPoolExecutor

from repair_agents import (
    MeaningPreservationAgent,
    GrammarOptimizedAgent,
    ConciseFluentAgent,
    SequenceOptimizedAgent
)


class RepairAgentsRunner:
    def __init__(self):
        self.agents = {
            "meaning_preservation_agent": MeaningPreservationAgent(),
            "grammar_optimized_agent": GrammarOptimizedAgent(),
            "concise_fluent_agent": ConciseFluentAgent(),
            "sequence_optimized_agent": SequenceOptimizedAgent()
        }

    def tokens_to_text(self, tokens):
        if isinstance(tokens, list):
            return " ".join(tokens)
        return str(tokens)

    def run_agent(self, agent_name, agent, original_text, prompt=None):
        repaired_text = agent.repair_text(original_text, prompt)

        #  Slight variation per agent (important for better selection)
        if agent_name == "sequence_optimized_agent":
            # preserve structure more
            repaired_text = repaired_text

        elif agent_name == "concise_fluent_agent":
            # extra cleanup for repetition
            import re
            repaired_text = re.sub(r'(.+?)\s+\1', r'\1', repaired_text)

        elif agent_name == "grammar_optimized_agent":
            # ensure punctuation
            if not repaired_text.endswith((".", "!", "?")):
                repaired_text += "."

        return {
            "agent_name": agent_name,
            "original_text": original_text,
            "repaired_text": repaired_text
        }

    def run_parallel(self, tokens, prompt=None):
        original_text = self.tokens_to_text(tokens)

        results = []

        with ThreadPoolExecutor() as executor:
            futures = []

            for agent_name, agent in self.agents.items():
                future = executor.submit(
                    self.run_agent,
                    agent_name,
                    agent,
                    original_text,
                    prompt
                )
                futures.append(future)

            for future in futures:
                results.append(future.result())

        return results