import helpers
from typing import Any
from django.conf import settings
from django.core.management.base import BaseCommand

STATICFILES_VENDOR_DIR = getattr(settings, 'STATICFILES_VENDOR_DIR')
VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.css",
    "flowbite.min.js": "https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js",
}

def remove_source_map_comment(file_path):
    if file_path.exists():
        content = file_path.read_text(encoding="utf-8").splitlines()
        cleaned = [line for line in content if "sourceMappingURL=flowbite.min.js.map" not in line]
        file_path.write_text("\n".join(cleaned), encoding="utf-8")

class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Downloading vendor static files")
        completed_urls = []
        for name, url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDOR_DIR / name
            dl_success = helpers.download_to_local(url, out_path)
            
        
            if dl_success and name == "flowbite.min.js":
                remove_source_map_comment(out_path)
                self.stdout.write(self.style.NOTICE("Removed sourceMappingURL from flowbite.min.js"))

            if dl_success:
                completed_urls.append(url)
            else:
                self.stdout.write(self.style.ERROR(f'Failed to download {url}'))

        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(self.style.SUCCESS('Successfully updated all vendor static files.'))
        else:
            self.stdout.write(self.style.WARNING('Some files were not updated.'))
