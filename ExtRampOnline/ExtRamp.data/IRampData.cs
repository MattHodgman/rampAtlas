using ExtRamp.core;
using System;
using System.Linq;
using System.Collections.Generic;
using System.IO;
using System.Text;


namespace ExtRamp.data
{
    public interface IRampData
    {
        IEnumerable<Ramp> GetAllRamps ();

    }
    
}
