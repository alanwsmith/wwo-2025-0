#!/usr/bin/env python3

from shutil import copy2
from string import Template

day_range = range(3, 32) 

themes = [
    "", "Transparency", "Maps", "Scramble", "Filters", "Remix", "Solids", "Sub-optimal", "Containers", "Blink", "Warning", "Camera", "Battle", "Upside-down", "Doubles", "Unicode", "Transition", "Illumination", "Trading", "Bounce", "Hidden", "Language", "Memory", "Style", "Counter", "Empty", "Texture", "Spell", "Tables", "Surprise", "Deprecated", "Spooky"
]

class Maker():
    def output_dir_for_day(self, day):
        return f"../../../wwo-2025-{day}/content/_wrappers"

    def copy_content_files(self):
        files = [
                "custom-styles.html",  
                "base-styles.html", 
                "bitty-data-send.txt", 
                "custom-head-tags.html"
                ]
        for day in day_range:
            for source_file in files:
                dest_path = f"{self.output_dir_for_day(day)}/{source_file}"
                print(dest_path)
                copy2(source_file, dest_path)

    def generate_wrapper(self, day):
        with open("main.html", "r") as _wrapper_in:
            skeleton = "".join(_wrapper_in.readlines())
            data = {
                    "THEME_VAR": themes[day],
                    "DAY_NUM_VAR": day,
                    "END_DAY_NUM_VAR": 31
                    }
            template = Template(skeleton)
            output = template.substitute(data)
            return output

    def output_wrapper(self, day):
        content = self.generate_wrapper(day)
        output_path = f"{self.output_dir_for_day(day)}/main.html"
        with open(output_path, "w") as _out:
            _out.write(content)


    def output_wrappers(self):
        for day in day_range:
            self.output_wrapper(day)

    def output_dir_for_js(self, day):
        return f"../../../wwo-2025-{day}/content/components"

    def copy_page_js_file(self, day):
        dest_path = f"{self.output_dir_for_js(day)}/page.js"
        copy2("page.js", dest_path)

    def copy_page_js_files(self):
        for day in day_range:
            self.copy_page_js_file(day)

if __name__ == "__main__":
    m = Maker()

    # Uncomment to do the files
    # m.copy_content_files()
    # m.output_wrappers()

