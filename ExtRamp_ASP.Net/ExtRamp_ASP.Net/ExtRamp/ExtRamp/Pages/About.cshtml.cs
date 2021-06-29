using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.AspNetCore.Mvc;
using System;

namespace ExtRamp.Pages
{
    public class AboutModel : PageModel
    {
        [BindProperty(SupportsGet = true)]
        public string Name { get; set; }
        public string Result { get; set; }
        [ViewData]
        public string Message { get; set; }

        public IActionResult OnGet()
        {
            return RedirectToPage("./Index");
        }


    }
}
