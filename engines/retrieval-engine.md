# Retrieval Engine Contract

`Source Registry -> Query Planner -> Retrieval Adapter -> Open/Inspect -> Authority Check -> Normalize -> Deduplicate -> Correlate -> Evidence -> Source Graph`

The retrieval engine supports both structured sources and web search. Each result records source, query, retrieval time, URL, status, and evidence pointer.

## Web search

The web-search adapter is provider-neutral. The runtime may bind it to Exa or another approved search provider. Provider credentials and endpoints are external configuration and are never hard-coded into the Skill.

## Opening sources

A search result is a lead. Material claims require source opening and validation against the canonical document. Redirects must remain within the approved domain policy and must never cross into private/internal address space.
