using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace ExtRamp.Pages
{
    public class PrivacyModel : PageModel
    {
        public IActionResult OnGet ()
        {
            return RedirectToPage("./Index");
        }
    }
}