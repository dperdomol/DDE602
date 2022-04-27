using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.PeerToPeer;
using System.Text;
using System.Threading.Tasks;

namespace Fileshare.Contracts.Repository
{
    public interface IPeerRegistrationRepository
    {
        bool IsPeerRegistered { get; }
        string PeerUri { get; }
        PeerName PeerName { get; set; }
        void StartPeerRegistration(string username, int port);
        void StopPeerRegistration();
    }
}
