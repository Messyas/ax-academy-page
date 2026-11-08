"""Apply the shared learning components to the existing page generator."""
import ast
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
p = root / 'generate-pages.py'
source = p.read_text(encoding='utf-8')
original_source = source
already_integrated = 'from learning_content import ' in source
tree = ast.parse(source)
lines = source.splitlines(keepends=True)
node = next(n for n in tree.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'course_sections' for t in n.targets))
lines[node.lineno - 1:node.end_lineno] = ['course_sections = render_course_modules(modules)\n']
source = ''.join(lines)
source = source.replace('from pathlib import Path\n', 'from pathlib import Path\nfrom learning_content import enrich_home, enrich_course, render_course_modules\n', 1)
source = source.replace("page('index.html'", "home = enrich_home(home)\npage('index.html'", 1)
source = source.replace("page('curso.html'", "course = enrich_course(course)\npage('curso.html'", 1)
source = source.replace("    html = f'''", "    learning_styles = '<link rel=\"stylesheet\" href=\"assets/learning.css\">' if filename in ('index.html', 'curso.html') else ''\n    learning_script = '<script src=\"assets/learning.js\" defer></script>' if filename in ('index.html', 'curso.html') else ''\n    html = f'''", 1)
source = source.replace('</head><body', '{learning_styles}</head><body', 1)
source = source.replace('<script src="assets/app.js" defer></script>', '{learning_script}<script src="assets/app.js" defer></script>', 1)
if already_integrated:
    source = original_source
else:
    p.write_text(source, encoding='utf-8')

# Render only the pages covered by this change, keeping the other pages intact.
tree = ast.parse(source)
page = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'page')
guard = ast.parse("if filename not in ('index.html', 'curso.html'):\n    return").body[0]
page.body.insert(0, guard)
ast.fix_missing_locations(tree)
sys.path.insert(0, str(root))
exec(compile(tree, str(p), 'exec'), {'__file__': str(p), '__name__': '__main__'})

