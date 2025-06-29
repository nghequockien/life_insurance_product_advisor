import streamlit.components.v1 as components


def render_mermaid(code: str):
    components.html(
        f"""
        <div class="mermaid">
        {code}
        </div>
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ theme: "default" }});
            mermaid.run();
        </script>
        """,
        height=600,
        scrolling=True,
    )
