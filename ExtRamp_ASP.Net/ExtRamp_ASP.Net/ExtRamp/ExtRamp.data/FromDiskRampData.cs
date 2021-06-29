using ExtRamp.core;
using System;
using System.Linq;
using System.Collections.Generic;
using System.Text;
using System.IO;

namespace ExtRamp.data
{
    public class FromDiskRampData : IRampData
    {
        readonly List<Ramp> ramps;
        
        public FromDiskRampData (string directoryLocation = @"C:\Users\Kyle\Desktop\ExtRamp\ExtRamp\ExtRamp\wwwroot\Data")
        {
            string[] files = Directory.GetFiles(directoryLocation, "*.fasta");
            ramps = new List<Ramp>();

            foreach (var file in files)
            {
                ramps.Add(new Ramp(Path.GetFileNameWithoutExtension(file), file, Path.ChangeExtension(file,".csv")));
            }
        }

        public IEnumerable<Ramp> GetAllRamps ()
        {
            return from r in ramps
                   orderby r.species
                   select r;
        }
    }
}
