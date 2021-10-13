using System;
using System.Collections.Generic;
using System.Text;

namespace ExtRamp.core
{
    public class Ramp
    {
        public string species;
        public string fastaFileName;
        public string csvFileName;

        public Ramp (string species, string fastaFileName, string csvFileName)
        {
            this.species = species;
            this.fastaFileName = fastaFileName;
            this.csvFileName = csvFileName;
        }
    }

}
