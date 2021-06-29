using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Security;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace ExtRamp.Pages
{
    public class SearchDatabaseModel : PageModel
    {
        /*
        [HttpGet("download-file/{fileId}")]
        public IActionResult DownloadFile(int fileId)
        {
            var filePath = GetFilePathFromId(fileId);
            if (filePath == null) return NotFound();

            return PhysicalFile(filePath, MimeTypes.GetMimeType(filePath), Path.GetFileName(filePath));
        }
        */

        

        [BindProperty]
        public string Filename { get; set; }

        public FileResult OnPost()
        {
            ViewData["filename"] = Filename;
            var filepath = AppDomain.CurrentDomain.BaseDirectory + "Ramp_percentages\\" + Filename;
            byte[] fileBytes = System.IO.File.ReadAllBytes(filepath);
            /*
            try
            {
                byte[] fileBytes = System.IO.File.ReadAllBytes(filepath);
                
            }
            catch (ArgumentException)
            {
                ViewData["filename"] = "ArgumentException";
            }
            catch (PathTooLongException)
            {
                ViewData["filename"] = "PathTooLongException";
            }
            catch (DirectoryNotFoundException e)
            {
                ViewData["filename"] = "DirectoryNotFoundException: " + filepath + " - " + e.Data + " - " + e.Message;
            }
            catch (IOException e)
            {
                ViewData["filename"] = "IOException: " + e.Message;
            }
            catch (UnauthorizedAccessException)
            {
                ViewData["filename"] = "UnauthorizedAccessException";
            }
            catch (NotSupportedException)
            {
                ViewData["filename"] = "NotSupportedException";
            }
            catch (SecurityException)
            {
                ViewData["filename"] = "SecurityException";
            }
            */
            return File(fileBytes, System.Net.Mime.MediaTypeNames.Application.Octet, Filename);

        }

        public void OnGet()
        {

        }
    }
}